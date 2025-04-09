import ProductList from "@/components/ProductList";
import React from "react";



const HomePage = async () => {
  return (
    <div className="container p-2 mt-5">
      <ProductList />
    </div>
  );
};

export default HomePage;
