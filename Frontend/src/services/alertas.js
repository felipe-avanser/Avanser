export const detectarAlertaRoja = () => {
  const reportes = JSON.parse(localStorage.getItem("reportes")) || [];
  const ahora = new Date();
  const recientes = reportes.filter((r) => {
    const fecha = new Date(r.fecha);
    const dias = (ahora - fecha) / (1000 * 60 * 60 * 24);
    return dias <= 10;
  });

  const porAprendiz = {};
  recientes.forEach((r) => {
    const nombre = r.nombre;
    porAprendiz[nombre] = porAprendiz[nombre] || [];
    porAprendiz[nombre].push(r);
  });

  return Object.entries(porAprendiz)
    .filter(([_, lista]) => lista.length >= 3)
    .map(([nombre]) => ({
      tipo: "Roja",
      aprendiz: nombre,
      mensaje: `Alerta Roja: ${nombre} tiene 3 reportes negativos en 10 días.`,
    }));
};

export const detectarAlertaAmarilla = () => {
  const reportes = JSON.parse(localStorage.getItem("reportes")) || [];
  const ahora = new Date();
  const porAprendiz = {};

  reportes.forEach((r) => {
    const fecha = new Date(r.fecha);
    const nombre = r.nombre;
    if (!porAprendiz[nombre] || porAprendiz[nombre] < fecha) {
      porAprendiz[nombre] = fecha;
    }
  });

  return Object.entries(porAprendiz)
    .filter(([_, fecha]) => {
      const dias = (ahora - fecha) / (1000 * 60 * 60 * 24);
      return dias >= 28;
    })
    .map(([nombre]) => ({
      tipo: "Amarilla",
      aprendiz: nombre,
      mensaje: `Alerta Amarilla: ${nombre} no ha sido reportado en 4 semanas.`,
    }));
};
