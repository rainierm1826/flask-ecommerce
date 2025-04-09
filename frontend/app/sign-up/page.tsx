"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FormEvent, useState } from "react";
import { signUp } from "@/api/user";

const SignUp = () => {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [confirmPassword, setConfirmPassword] = useState<string>("");

  const handleSignUp = async (e:FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    try {
      if (password !== confirmPassword) {
        return console.log("not match");
      }

      const response = await signUp({ email, password });
      console.log(response);
      return response;
    } catch (error) {
      return error;
    }
  };

  return (
    <div className="flex justify-center items-center h-[calc(100vh-60px)]">
      <div className="shadow-sm py-4 px-10 rounded-sm">
        <h1 className="text-center text-2xl font-bold mb-10">Sign Up</h1>
        <form onSubmit={handleSignUp}>
          <Label>Email</Label>
          <Input
            placeholder="email"
            className="mt-2 mb-5"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Label>Password</Label>
          <Input
            placeholder="password"
            type="password"
            className="mt-2 mb-5"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Label>Confirm Password</Label>
          <Input
            placeholder="confirm password"
            type="password"
            className="mt-2 mb-5"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
          <div className="flex justify-end">
            <Button>Sign Up</Button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignUp;
