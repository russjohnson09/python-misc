import type { Route } from "./+types/home";
import { Welcome } from "../welcome/welcome";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New React Router App 2" },
    { name: "description", content: "Welcome to React Router! 2" },
  ];
}

// https://chessboardjs.com/
export default function About() {
  return <><h1>Chess</h1></>;
}
