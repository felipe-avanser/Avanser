from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.db import transaction
from django.utils.crypto import get_random_string
import csv
import io

from apps.usuario.models import Usuario, Rol
from apps.coordinador_area.models import Area, AsignacionInstructorArea


class InstructorCSVUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        print("DEBUG Content-Type:", request.META.get("CONTENT_TYPE"))
        print("DEBUG data keys:", list(request.data.keys()))
        print("DEBUG FILES keys:", list(request.FILES.keys()))

        csv_file = request.FILES.get("file")
        if not csv_file:
            return Response(
                {"message": "No se adjuntó archivo CSV.", "files_keys": list(request.FILES.keys())},
                status=400
            )

        if not csv_file.name.endswith(".csv"):
            return Response({"message": "El archivo debe ser .csv"}, status=400)

        decoded = csv_file.read().decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(decoded))

        required_columns = {"username", "first_name", "last_name", "email", "area", "coordinador_username"}
        if not required_columns.issubset(reader.fieldnames):
            return Response(
                {"message": "Faltan columnas obligatorias.", "esperadas": list(required_columns)},
                status=400
            )

        rol_instructor, _ = Rol.objects.get_or_create(nombre="Instructor")

        resultados = []

        with transaction.atomic():
            for row in reader:

                username = row["username"].strip()
                area_name = row["area"].strip()
                coor_username = row["coordinador_username"].strip()

                # 1. Buscar coordinador
                try:
                    coordinador = Usuario.objects.get(username=coor_username)
                except Usuario.DoesNotExist:
                    resultados.append({
                        "username": username,
                        "error": f"Coordinador '{coor_username}' no existe."
                    })
                    continue

                # 2. Crear/actualizar instructor
                temp_pass = None
                user, created = Usuario.objects.get_or_create(
                    username=username,
                    defaults={
                        "first_name": row["first_name"],
                        "last_name": row["last_name"],
                        "email": row["email"],
                        "rol": rol_instructor
                    }
                )

                if created:
                    temp_pass = get_random_string(8)
                    user.set_password(temp_pass)
                    user.save()
                else:
                    user.first_name = row["first_name"]
                    user.last_name = row["last_name"]
                    user.email = row["email"]
                    user.rol = rol_instructor
                    user.save()

                # 3. Crear área si no existe
                area, _ = Area.objects.get_or_create(nombre=area_name)

                # 4. Asignación Instructor–Área
                asignacion, crea_asig = AsignacionInstructorArea.objects.get_or_create(
                    instructor=user,
                    area=area,
                    defaults={"coordinador": coordinador}
                )

                estado = "nuevo" if crea_asig else "ya_asignado"

                resultados.append({
                    "username": username,
                    "area": area_name,
                    "coordinador": coor_username,
                    "temp_password": temp_pass,
                    "estado": estado
                })

        return Response(
            {"message": "Archivo procesado correctamente.", "data": resultados},
            status=200
        )
