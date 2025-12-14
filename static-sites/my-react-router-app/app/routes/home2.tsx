import type { Route } from "./+types/home";
import { Welcome } from "../welcome/welcome";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New React Router App 2" },
    { name: "description", content: "Welcome to React Router! 2" },
  ];
}

export default function Home() {
  return <Welcome />;
}
