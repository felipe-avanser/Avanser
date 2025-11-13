import { useState } from "react";
import { Upload, FileText, CheckCircle2, AlertCircle, Info } from "lucide-react";

const GenerarPerfiles = () => {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("");
  const [uploading, setUploading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState("");
  const [serverMessage, setServerMessage] = useState("");
  const [data, setData] = useState([]);

  // Seleccionar CSV
  const handleFileSelect = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    if (!selectedFile.name.endsWith(".csv")) {
      setError("El archivo debe ser formato .csv");
      setFile(null);
      setFileName("");
      return;
    }

    setFile(selectedFile);
    setFileName(selectedFile.name);
    setError("");
    setSuccess(false);
    setData([]);
    setServerMessage("");
  };

  // Enviar CSV al backend
  const handleUploadToBackend = async () => {
    if (!file) {
      setError("Selecciona un archivo CSV antes de continuar.");
      return;
    }

    setUploading(true);
    setError("");
    setSuccess(false);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/coordinador/upload-instructores/",
        {
          method: "POST",
          body: formData,
        }
      );

      const rawText = await response.text();
      let result;

      try {
        result = JSON.parse(rawText);
      } catch {
        throw new Error("El servidor devolvió una respuesta no válida.\n" + rawText);
      }

      if (!response.ok) {
        setError(result.message || "Error procesando el archivo.");
        setSuccess(false);
        return;
      }

      setServerMessage(result.message || "Archivo procesado correctamente.");
      setData(result.data || []);
      setSuccess(true);

    } catch (err) {
      console.error("Error:", err);
      setError(err.message || "Error inesperado.");
      setSuccess(false);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 py-10 px-6">
      <div className="max-w-5xl mx-auto bg-white shadow-lg rounded-2xl p-8 border border-gray-100">

        <h1 className="text-4xl font-bold text-gray-800 mb-4 text-center">
          Generar Perfiles de Instructores
        </h1>

        <p className="text-gray-500 text-center mb-6">
          Sube un archivo CSV. El sistema creará los usuarios con rol{" "}
          <b>Instructor</b>, los asignará a un <b>Área</b> y los vinculará con un{" "}
          <b>Coordinador de Área</b>.
        </p>

        {/* Cuadro informativo CSV */}
        <div className="mb-8 rounded-xl border border-blue-100 bg-blue-50/70 p-4 flex gap-3 items-start">
          <Info className="w-5 h-5 text-blue-600 mt-0.5" />
          <div className="text-sm text-gray-700">
            <p className="font-semibold text-blue-700 mb-1">
              Formato obligatorio del CSV:
            </p>
            <p>
              Columnas:{" "}
              <code className="bg-white px-1 py-0.5 rounded border">
                username, first_name, last_name, email, area, coordinador_username
              </code>
            </p>

            <p className="mt-2 text-xs text-gray-500">
              Ejemplo:{" "}
              <code>
                daniel1,Daniel,Perez,daniel@gmail.com,ADSO,coord_adso
              </code>
            </p>
          </div>
        </div>

        {/* Zona de carga */}
        <div className="flex flex-col items-center justify-center gap-5 border-2 border-dashed border-blue-300 rounded-xl py-10 bg-blue-50/30 hover:bg-blue-50 transition">
          <Upload className="w-12 h-12 text-blue-500" />

          <label className="cursor-pointer">
            <input
              type="file"
              accept=".csv"
              onChange={handleFileSelect}
              className="hidden"
            />
            <span className="px-5 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition">
              Seleccionar archivo
            </span>
          </label>

          {fileName && (
            <div className="flex items-center gap-2 text-sm text-gray-600">
              <FileText className="w-4 h-4 text-blue-500" />
              <span>Archivo seleccionado: {fileName}</span>
            </div>
          )}
        </div>

        {/* Botón procesar */}
        <div className="text-center mt-6">
          <button
            onClick={handleUploadToBackend}
            disabled={uploading}
            className={`px-8 py-3 rounded-lg text-white font-medium shadow transition ${uploading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-gradient-to-r from-blue-600 to-indigo-600 hover:shadow-lg hover:scale-[1.02]"
              }`}
          >
            {uploading ? "Subiendo..." : "Procesar CSV"}
          </button>

          {/* Éxito */}
          {success && (
            <div className="mt-4 flex flex-col items-center justify-center text-green-600 font-semibold">
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-5 h-5" />
                <span>{serverMessage}</span>
              </div>
            </div>
          )}

          {/* Error */}
          {error && (
            <div className="mt-4 flex items-center justify-center text-red-600 font-semibold gap-2">
              <AlertCircle className="w-5 h-5" />
              <span>{error}</span>
            </div>
          )}
        </div>

        {/* Tabla de resultados */}
        {data.length > 0 && (
          <div className="mt-10 overflow-x-auto animate-fadeIn">
            <h2 className="text-lg font-semibold text-gray-800 mb-3">
              Resultado del procesamiento
            </h2>

            <table className="min-w-full border border-gray-200 rounded-lg overflow-hidden shadow-sm text-sm">
              <thead className="bg-blue-600 text-white">
                <tr>
                  {Object.keys(data[0]).map((key) => (
                    <th
                      key={key}
                      className="px-4 py-2 text-left uppercase tracking-wider font-semibold"
                    >
                      {key}
                    </th>
                  ))}
                </tr>
              </thead>

              <tbody>
                {data.map((row, idx) => (
                  <tr
                    key={idx}
                    className={
                      idx % 2 === 0 ? "bg-white" : "bg-blue-50 hover:bg-blue-100"
                    }
                  >
                    {Object.values(row).map((value, i) => (
                      <td key={i} className="px-4 py-2 text-gray-700 border-b">
                        {String(value)}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

      </div>
    </div>
  );
};

export default GenerarPerfiles;
