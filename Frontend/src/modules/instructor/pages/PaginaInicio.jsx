import React from "react";
import { Link } from "react-router-dom";
import { Users, BarChart2, Bell, BookOpen, UserPlus } from "react-feather";

// Importaciones
import Navbar from "../../components/Navbar.jsx";
import { AlertCircle } from "lucide-react";

const PaginaInicio = () => {
  const accesos = [
    { nombre: "Instructores", icon: <Users size={32} color="green" />, ruta: "/usuarios" },
    { nombre: "Rendimiento", icon: <BarChart2 size={32} color="green"/>, ruta: "/rendimiento" },
    { nombre: "Reportes", icon: <AlertCircle size={32}  color="green"/>, ruta: "/notificaciones" },
   
  ];

  return (
    <div className="p-8 bg-gray-100 min-h-screen t-8">

    <Navbar />
      <h1 className="text-6xl font-bold mb-6 text-gray-800 ml-5">
        <span className="Block">Bienvenido Instructor</span>
        <br />
        <span className="text-green-600">Franco Reina</span>
    
      </h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-10">
        {accesos.map((item, i) => (
          <Link
            to={item.ruta}
            key={i}
            className="flex flex-col items-center justify-center bg-white shadow-md rounded-2xl p-6 hover:shadow-lg hover:bg-gray-50 transition transform hover:-translate-y-1 mt-8"
          >
            <div className="text-indigo-600 mb-3">{item.icon}</div>
            <h3 className="text-lg font-medium">{item.nombre}</h3>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default PaginaInicio;
