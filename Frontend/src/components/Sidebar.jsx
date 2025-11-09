// Barra lateral del sistema (navegación entre secciones).import React, { useState } from "react";
import {
  Home,
  BarChart2,
  Users,
  BookOpen,
  UserPlus,
  User,
  LogOut,
  ChevronLeft,
} from "react-feather";

const Sidebar = () => {
  const [open, setOpen] = useState(true);
  const [showConfirm, setShowConfirm] = useState(false);

  const menus = [
    { title: "Inicio", icon: <Home size={20} /> },
    { title: "Rendimiento", icon: <BarChart2 size={20} /> },
    { title: "Usuarios", icon: <Users size={20} /> },
    { title: "Fichas", icon: <BookOpen size={20} /> },
    { title: "Creación de Instructores", icon: <UserPlus size={20} /> },
    { title: "Perfil", icon: <User size={20} /> },
  ];

  const handleLogout = () => {
    setShowConfirm(true);
  };

  const confirmLogout = (confirm) => {
    setShowConfirm(false);
    if (confirm) {
      alert("Sesión cerrada correctamente.");
      // Aquí podrías redirigir al login, por ejemplo:
      // window.location.href = "/login";
    }
  };

  return (
    <div
      className={`${
        open ? "w-64" : "w-20"
      } bg-gray-900 text-white min-h-screen p-5 pt-8 relative duration-300 flex flex-col justify-between`}
    >
      {/* Botón para colapsar */}
      <ChevronLeft
        className={`absolute cursor-pointer -right-3 top-9 w-7 border-2 border-gray-700 bg-gray-900 rounded-full transform ${
          !open && "rotate-180"
        }`}
        onClick={() => setOpen(!open)}
      />

      {/* Contenido principal */}
      <div>
        {/* Logo */}
        <div className="flex gap-x-4 items-center mb-8">
          <img
            src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png"
            className={`cursor-pointer duration-500 w-10 ${
              open && "rotate-[360deg]"
            }`}
          />
          <h1
            className={`text-white origin-left font-medium text-xl duration-200 ${
              !open && "scale-0"
            }`}
          >
            Avanser
          </h1>
        </div>

        {/* Menú */}
        <ul className="pt-2">
          {menus.map((menu, index) => (
            <li
              key={index}
              className="flex items-center gap-x-4 cursor-pointer p-2 hover:bg-gray-700 rounded-md mt-2 text-sm"
            >
              {menu.icon}
              <span className={`${!open && "hidden"} origin-left duration-200`}>
                {menu.title}
              </span>
            </li>
          ))}
        </ul>
      </div>

      {/* Botón de cerrar sesión */}
      <div>
        <button
          onClick={handleLogout}
          className="flex items-center gap-x-4 cursor-pointer p-2 hover:bg-red-600 rounded-md text-sm w-full justify-center"
        >
          <LogOut size={20} />
          <span className={`${!open && "hidden"} origin-left duration-200`}>
            Cerrar sesión
          </span>
        </button>

        {/* Ventana de confirmación */}
        {showConfirm && (
          <div className="absolute bottom-20 left-1/2 transform -translate-x-1/2 bg-gray-800 border border-gray-700 p-4 rounded-lg w-64 text-center shadow-lg">
            <p className="text-sm mb-3">¿Seguro que deseas cerrar sesión?</p>
            <div className="flex justify-around">
              <button
                onClick={() => confirmLogout(true)}
                className="bg-red-600 px-3 py-1 rounded hover:bg-red-700"
              >
                Sí
              </button>
              <button
                onClick={() => confirmLogout(false)}
                className="bg-gray-600 px-3 py-1 rounded hover:bg-gray-700"
              >
                No
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Sidebar;
