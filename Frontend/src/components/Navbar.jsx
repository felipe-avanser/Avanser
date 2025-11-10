import { Bell } from "lucide-react";

const Navbar = () => {
  return (
    <nav className="   p-2 flex justify-end items-top ">
      <button className="relative p-2 rounded-full hover:bg-gray-100">
        <Bell className="w-6 h-6 text-gray-700" />
        <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
      </button>
    </nav>
  );
};

export default Navbar;
