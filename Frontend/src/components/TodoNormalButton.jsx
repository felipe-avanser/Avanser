const TodoNormalButton = ({ grupo }) => {
  const registrarTodoNormal = () => {
    const registro = {
      grupo,
      fecha: new Date().toISOString(),
      estado: 'Todo Normal',
    };
    const prev = JSON.parse(localStorage.getItem('novedades')) || [];
    localStorage.setItem('novedades', JSON.stringify([...prev, registro]));
    alert('Estado registrado como Todo Normal');
  };

  return (
    <button className="btn bg-gray-500 text-white" onClick={registrarTodoNormal}>
      Todo Normal
    </button>
  );
};

export default TodoNormalButton;
