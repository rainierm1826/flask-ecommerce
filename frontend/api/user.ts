import { CredentialTypes } from "@/lib/types";
import axios from "axios";

const user = axios.create({
  baseURL: "http://localhost:5000/user",
  withCredentials: true,
});

export const signUp = async ({ email, password }: CredentialTypes) => {
  try {
    const { data } = await user.post("/sign-up", {
      email,
      password,
    });

    return data;
  } catch (error) {
    return error;
  }
};

export const signIn = async ({ email, password }: CredentialTypes) => {
  try {
    const { data } = await user.post("/sign-in", {
      email,
      password,
    });
    return data;
  } catch (error) {
    return error;
  }
};

export const fetchUserInfo = async (token: string) => {
  try {
    const { data } = await user.get("/get-user", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return data;
  } catch (error) {
    return error;
  }
};
