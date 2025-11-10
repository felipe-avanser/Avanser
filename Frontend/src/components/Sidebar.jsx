import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  FaHome,
  FaChartBar,
  FaUsers,
  FaBookOpen,
  FaUserPlus,
  FaUser,
  FaSignOutAlt,
  FaClipboardList,
  FaFileAlt,
  FaBolt,
  FaBell,
} from "react-icons/fa";

const Sidebar = () => {
  const [open, setOpen] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);
  const navigate = useNavigate();

  const menus = [
    { title: "Dashboard", icon: <FaHome size={18} />, path: "/dashboard-final" },
    { title: "Reportes", icon: <FaFileAlt size={18} />, path: "/reportes" },
    { title: "Citación", icon: <FaClipboardList size={18} />, path: "/citacion" },
    { title: "Reporte Rápido", icon: <FaBolt size={18} />, path: "/rapido" },
    { title: "Historial Aprendiz", icon: <FaUsers size={18} />, path: "/historial" },
    { title: "Check-in", icon: <FaBookOpen size={18} />, path: "/checkin" },
    { title: "Bienestar", icon: <FaUserPlus size={18} />, path: "/bienestar" },
    { title: "Historial Bienestar", icon: <FaUser size={18} />, path: "/historial-bienestar" },
    { title: "Dashboard Gráficas", icon: <FaChartBar size={18} />, path: "/dashboard-charts" },
    { title: "Dashboard General", icon: <FaChartBar size={18} />, path: "/dashboard-general" },
    { title: "Push Check-in", icon: <FaBell size={18} />, path: "/push-checkin" },
  ];

  const handleLogout = () => {
    setShowConfirm(true);
  };

  const confirmLogout = (confirm) => {
    setShowConfirm(false);
    if (confirm) {
      alert("Sesión cerrada correctamente.");
      // navigate("/login");
    }
  };

  return (
    <>
      {/* Sidebar principal */}
      <div
        onMouseEnter={() => setOpen(true)}
        onMouseLeave={() => setOpen(false)}
        className={`${
          open ? "w-64" : "w-20"
        } bg-white text-gray-800 shadow-2xl min-h-screen p-4 pt-6 relative duration-300 flex flex-col`}
      >
        {/* Logo y título */}
        <div className="flex gap-x-3 items-center mb-6">
          <img
            src="https://oficinavirtualderadicacion.sena.edu.co/oficinavirtual/Resources/logoSenaNaranja.png"
            alt="logo"
            className="w-14 h-14"
          />
          <h1
            className={`origin-left font-bold text-2xl tracking-wide duration-300 ${
              !open && "scale-0"
            }`}
          >
            Avanser
          </h1>
        </div>

        {/* Menús scrolleables */}
        <ul className="flex-1 overflow-y-auto pr-2 space-y-2 scrollbar-thin scrollbar-thumb-gray-400 scrollbar-track-gray-100">
          {menus.map((menu, index) => (
            <li key={index}>
              <Link
                to={menu.path}
                className="flex items-center gap-x-4 p-2 rounded-lg hover:bg-green-600 hover:text-white transition-all duration-200"
              >
                <span>{menu.icon}</span>
                <span
                  className={`text-sm font-medium ${
                    !open && "hidden"
                  } duration-200`}
                >
                  {menu.title}
                </span>
              </Link>
            </li>
          ))}
        </ul>

        {/* Botón de cerrar sesión */}
        <div className="mt-4">
          <button
            onClick={handleLogout}
            className="flex items-center gap-x-4 p-2 rounded-lg w-full justify-center bg-red-600 hover:bg-red-700 text-white transition-all duration-200"
          >
            <FaSignOutAlt size={18} />
            <span className={`${!open && "hidden"} origin-left text-sm`}>
              Cerrar sesión
            </span>
          </button>
        </div>
      </div>

      {/* Modal de confirmación */}
      {showConfirm && (
        <div className="fixed inset-0 bg-black bg-opacity-60 flex justify-center items-center z-50">
          <div className="bg-white text-gray-800 p-8 rounded-2xl shadow-2xl w-80 text-center">
            <h2 className="text-lg font-semibold mb-4">
              ¿Seguro que deseas cerrar sesión?
            </h2>
            <div className="flex justify-around mt-4">
              <button
                onClick={() => confirmLogout(true)}
                className="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700 transition-all"
              >
                Sí
              </button>
              <button
                onClick={() => confirmLogout(false)}
                className="bg-gray-400 text-white px-4 py-2 rounded-md hover:bg-gray-500 transition-all"
              >
                No
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Sidebar;
