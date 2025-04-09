import React from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "./ui/button";
import Image from "next/image";
import { CardTypes } from "@/lib/types";

const ProductCard = ({
  productName,
  productPrice,
  productImage,
}: CardTypes) => {
  return (
    <Card>
      <CardContent className="flex justify-center items-center">
        <Image
          src={productImage}
          alt=""
          width={150}
          height={150}
          unoptimized={true}
        />
      </CardContent>
      <CardHeader>
        <CardTitle>{productName}</CardTitle>
        <CardDescription>₱ {productPrice}</CardDescription>
      </CardHeader>
      <CardFooter>
        <Button className="cursor-pointer">Buy Now</Button>
      </CardFooter>
    </Card>
  );
};

export default ProductCard;
