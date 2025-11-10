import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import DashboardFinal from "../modules/instructor/pages/DashboardFinal";
import ReportesPage from "../modules/instructor/pages/ReportesPage";
import CitacionForm from "../modules/instructor/pages/CitacionForm";
import ReporteRapido from "../modules/instructor/pages/ReporteRapido";
import HistorialAprendiz from "../modules/instructor/pages/HistorialAprendiz";
import CheckInPeriodico from "../modules/instructor/pages/CheckInPeriodico";
import BienestarComunicacion from "../modules/instructor/pages/BienestarComunicacion";
import HistorialBienestar from "../modules/instructor/pages/HistorialBienestar";
import DashboardCharts from "../modules/instructor/pages/DashboardCharts";
import DashboardGeneral from "../modules/instructor/pages/DashboardGeneral";
import PushCheckIn from "../components/PushCheckIn";
import Navbar from "../components/Navbar"


const AppRouter = () => {
  return (
    <Router>
      <div className="flex">
        <Sidebar />
       
        <div className="flex-1 p-6">
          <Routes>
            {/* ✅ Redirección: "/" va directo al DashboardFinal */}
            <Route path="/" element={<Navigate to="/dashboard-final" replace />} />

            <Route path="/dashboard-final" element={<DashboardFinal />} />
            <Route path="/reportes" element={<ReportesPage />} />
            <Route path="/citacion" element={<CitacionForm />} />
            <Route path="/rapido" element={<ReporteRapido />} />
            <Route path="/historial" element={<HistorialAprendiz />} />
            <Route path="/checkin" element={<CheckInPeriodico />} />
            <Route path="/bienestar" element={<BienestarComunicacion />} />
            <Route path="/historial-bienestar" element={<HistorialBienestar />} />
            <Route path="/dashboard-charts" element={<DashboardCharts />} />
            <Route path="/dashboard-general" element={<DashboardGeneral />} />
            <Route path="/push-checkin" element={<PushCheckIn />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default AppRouter;
