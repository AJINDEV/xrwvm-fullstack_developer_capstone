import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // Import the new component
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} /> {/* Add the new route */}
    </Routes>
  );
}
export default App;
