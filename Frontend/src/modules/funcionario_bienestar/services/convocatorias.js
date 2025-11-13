export const guardarConvocatoria = (convocatoria) => {
  const prev = JSON.parse(localStorage.getItem("convocatorias")) || [];
  const nueva = {
    ...convocatoria,
    id: Date.now(),
    estado: "Borrador",
  };
  localStorage.setItem("convocatorias", JSON.stringify([...prev, nueva]));
  return nueva;
};

