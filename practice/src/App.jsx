import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import SignIn from "./pages/Auth/SignIn";
import SignUp from "./pages/Auth/SignUp";
import LogOutHome from "./pages/Home/LogOutHome";
import LogInHome from "./pages/Home/LogInHome";
import Header from "./components/common/Header";

const App = () => {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/" element={<LogOutHome />} />
        <Route path="/home" element={<LogInHome />} />
      </Routes>
    </div>
  );
};

export default App;
