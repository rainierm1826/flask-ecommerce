import axios from "axios";

const product = axios.create({
  baseURL: "http://localhost:5000/product",
});

export const getProducts = async () => {
  try {
    const { data } = await product.get("/get-products");
    return data.product;
  } catch (error) {
    return error;
  }
};
