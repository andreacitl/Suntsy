import { BrowserRouter, Routes, Route } from "react-router-dom";
import GetStarted from "./pages/GetStarted";
import SignUp from "./pages/SignUp";
import LogIn from "./pages/LoginPage";
import principal from "./pages/MainPage";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/getstarted" element={<GetStarted/>} />
        <Route path="/signup" element={<SignUp/>} />
        <Route path="/login" element={<LogIn/>} />
        <Route path="/" element={<principal/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
