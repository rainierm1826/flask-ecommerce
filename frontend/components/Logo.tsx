import Link from "next/link";
import React from "react";

const Logo = () => {
  return (
    <Link href={"/"}>
      <h1 className="text-4xl tracking-widest">logo</h1>
    </Link>
  );
};

export default Logo;
