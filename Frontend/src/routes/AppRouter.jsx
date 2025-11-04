import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LoginPage from '../modules/usuario/pages/LoginPage';
import RegisterPage from '../modules/usuario/pages/RegisterPage';
import InstructorDashboard from '../modules/instructor/pages/InstructorDashboard';
import AreaDashboard from '../modules/coordinador_area/pages/AreaDashboard';
import ProtectedRoute from '../components/ProtectedRoute';

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/instructor" element={<InstructorDashboard />} />
          <Route path="/coordinador" element={<AreaDashboard />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
