import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const InscripcionConvocatoria = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [convocatoria, setConvocatoria] = useState(null);
  const [nombre, setNombre] = useState("");
  const [documento, setDocumento] = useState("");

  useEffect(() => {
    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    const encontrada = todas.find((c) => c.id === Number(id));
    setConvocatoria(encontrada);
  }, [id]);

  const handleInscripcion = () => {
    if (!nombre || !documento) {
      alert("⚠️ Por favor completa todos los campos.");
      return;
    }

    if (convocatoria.inscripciones?.length >= Number(convocatoria.cupos)) {
      alert("❌ Ya no hay cupos disponibles.");
      return;
    }

    const nuevaInscripcion = {
      nombre,
      documento,
      fecha: new Date().toLocaleDateString(),
    };

    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    const actualizadas = todas.map((c) =>
      c.id === Number(id)
        ? {
            ...c,
            inscripciones: [...(c.inscripciones || []), nuevaInscripcion],
          }
        : c
    );

    localStorage.setItem("convocatorias", JSON.stringify(actualizadas));
    alert("✅ Inscripción realizada exitosamente");
    navigate(`/detalle-convocatoria/${id}`);
  };

  if (!convocatoria) {
    return <div className="p-6 text-center">Convocatoria no encontrada.</div>;
  }

  if (convocatoria.estado !== "Activa") {
    return (
      <div className="p-6 text-center">
        La convocatoria no está disponible para inscripciones.
      </div>
    );
  }

  return (
    <div className="p-6 max-w-2xl mx-auto bg-white rounded shadow-md">
      <h2 className="text-2xl font-bold mb-4">
        Inscribirse en {convocatoria.titulo}
      </h2>

      <label className="block mb-2 font-semibold">Nombre completo</label>
      <input
        type="text"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        className="w-full p-2 border border-gray-300 rounded mb-4"
        placeholder="Tu nombre"
      />

      <label className="block mb-2 font-semibold">Documento</label>
      <input
        type="text"
        value={documento}
        onChange={(e) => setDocumento(e.target.value)}
        className="w-full p-2 border border-gray-300 rounded mb-4"
        placeholder="Número de documento"
      />

      <button
        onClick={handleInscripcion}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-all"
      >
        Inscribirme
      </button>
    </div>
  );
};

export default InscripcionConvocatoria;
