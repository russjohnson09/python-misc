import { type RouteConfig, index, route } from "@react-router/dev/routes";

// https://reactrouter.com/upgrading/remix#4-add-a-routests-file
// https://reactrouter.com/start/framework/routing
export default [
    index("routes/home.tsx"), 
    // index("routes/home2.tsx")
    route("about", "routes/about.tsx"),

    route("home2", "routes/home2.tsx"),
    route("chess", "routes/chess.tsx"),


] satisfies RouteConfig;
// export default [index("routes/home2.tsx")] satisfies RouteConfig;
