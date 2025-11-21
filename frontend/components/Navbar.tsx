"use client";

import React from "react";
import { Navbar } from "flowbite-react";
import ThemeSwitcher from "./ThemeButton";

const NavbarComponent = () => {
  return (
    <>
      <Navbar fluid={true} rounded={true}>
        <Navbar.Brand href="/">
          <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
            Smart Kidney: AI-Powered CT Scan Classification System 
          </span>
        </Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse>
          <ThemeSwitcher />
        </Navbar.Collapse>
      </Navbar>
    </>
  );
};

export default NavbarComponent;
