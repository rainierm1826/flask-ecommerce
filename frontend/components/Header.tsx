"use client";

import Logo from "./Logo";
import Link from "next/link";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { NAV_LINKS } from "@/lib/staticObj";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { useSelector } from "react-redux";
const Header = () => {
  const userInfo = useSelector(state => state.user.user)
  console.log(userInfo)

  return (
    <header className="flex justify-between items-center container h-[60px] px-2">
      {/* logo */}
      <div className="flex items-center gap-5">
        <Logo />
        <Badge className="cursor-pointer" variant={"secondary"}>
          <Link href={"/admin/sign-in"}>admin</Link>
        </Badge>
      </div>

      {/* navlinks */}
      <div className="flex items-center gap-8 capitalize">
        {NAV_LINKS.map((links, index) => (
          <Link key={index} href={links.href} className="">
            {links.link}
          </Link>
        ))}
        {!userInfo ? (
          <div className="flex gap-2">
            <Link href={"/sign-up"}>
              <Button
                variant={"outline"}
                className="rounded-full cursor-pointer"
              >
                Sign Up
              </Button>
            </Link>
            <Link href={"/sign-in"}>
              <Button className="rounded-full cursor-pointer">Sign In</Button>
            </Link>
          </div>
        ) : (
          <div className="flex gap-2 items-center font-bold">
            <p className="text-black">{userInfo}</p>
            <Avatar>
              <AvatarImage src="https://github.com/shadcn.png" />
              <AvatarFallback>{userInfo}</AvatarFallback>
            </Avatar>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;
