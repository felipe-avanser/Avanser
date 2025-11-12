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
import ListadoConvocatorias from "../modules/funcionario_bienestar/pages/ListadoConvocatoriasTemp";
import EditarConvocatoria from "../modules/funcionario_bienestar/pages/EditarConvocatoria";
import DetalleConvocatoria from "../modules/funcionario_bienestar/pages/DetalleConvocatoria";
import FormularioConvocatoria from "../modules/funcionario_bienestar/pages/FormularioConvocatoria";
import InscripcionConvocatoria from "../modules/funcionario_bienestar/pages/InscripcionConvocatoria";
import VistaAprendizConvocatorias from "../modules/funcionario_bienestar/pages/VistaAprendizConvocatorias";

const AppRouter = () => {
  return (
    <Router>
      <div className="flex">
        <Sidebar />
       
        <div className="flex-1 p-6">
          <Routes>
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
            <Route path="/convocatorias" element={<ListadoConvocatorias />} />
            <Route path="/editar-convocatoria/:id" element={<EditarConvocatoria />} />
            <Route path="/detalle-convocatoria/:id" element={<DetalleConvocatoria />} />
            <Route path="/crear-convocatoria" element={<FormularioConvocatoria />} />
            <Route path="/inscripcion-convocatoria/:id" element={<InscripcionConvocatoria />} />
            <Route path="/convocatorias-aprendiz" element={<VistaAprendizConvocatorias />} />
            
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default AppRouter;
