import { useState } from "react";
import { useNavigate } from "react-router-dom";

const FormularioConvocatoria = () => {
  const navigate = useNavigate();
  const [convocatoria, setConvocatoria] = useState({
    titulo: "",
    tipo: "",
    inicio: "",
    cierre: "",
    cupos: "",
    descripcion: "",
  });

  const handleChange = (e) => {
    setConvocatoria({ ...convocatoria, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validación de fechas
    const fechaInicio = new Date(convocatoria.inicio);
    const fechaCierre = new Date(convocatoria.cierre);

    if (fechaCierre <= fechaInicio) {
      alert("❌ La fecha de cierre debe ser posterior a la fecha de inicio.");
      return;
    }

    // Guardar convocatoria en localStorage
    const todas = JSON.parse(localStorage.getItem("convocatorias")) || [];
    const nueva = {
      ...convocatoria,
      id: Date.now(),
      estado: "Borrador",
      inscripciones: [],
      historial: [
        { estado: "Borrador", fecha: new Date().toLocaleString() }
      ],
    };
    todas.push(nueva);
    localStorage.setItem("convocatorias", JSON.stringify(todas));

    alert("✅ Convocatoria creada exitosamente en estado Borrador");
    navigate(`/detalle-convocatoria/${nueva.id}`);
  };

  return (
    <div className="p-6 max-w-3xl mx-auto bg-white rounded shadow-md">
      <h2 className="text-2xl font-bold mb-4">Crear Convocatoria</h2>
      <form onSubmit={handleSubmit}>
        <label className="block mb-2 font-semibold">Título</label>
        <input
          type="text"
          name="titulo"
          value={convocatoria.titulo}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Tipo</label>
        <input
          type="text"
          name="tipo"
          value={convocatoria.tipo}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Fecha de inicio</label>
        <input
          type="date"
          name="inicio"
          value={convocatoria.inicio}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Fecha de cierre</label>
        <input
          type="date"
          name="cierre"
          value={convocatoria.cierre}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Cupos disponibles</label>
        <input
          type="number"
          name="cupos"
          value={convocatoria.cupos}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <label className="block mb-2 font-semibold">Descripción</label>
        <textarea
          name="descripcion"
          value={convocatoria.descripcion}
          onChange={handleChange}
          className="w-full p-2 border rounded mb-4"
          required
        />

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-all"
        >
          Guardar convocatoria
        </button>
      </form>
    </div>
  );
};

export default FormularioConvocatoria;
