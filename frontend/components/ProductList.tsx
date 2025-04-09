import React from "react";
import ProductCard from "./ProductCard";
import { getProducts } from "@/api/product";
import { ProductTypes } from "@/lib/types";

const products = await getProducts();

const ProductList = () => {
  return (
    <div className="grid grid-cols-4 gap-5">
      {products.map((product: ProductTypes) => (
        <ProductCard
          key={product.pid}
          productImage={product.product_image}
          productName={product.product_name}
          productPrice={product.product_price}
        />
      ))}
    </div>
  );
};

export default ProductList;
