// https://docs.netlify.com/build/frameworks/framework-setup-guides/express/
// https://docs.netlify.com/build/functions/get-started/?data-tab=TypeScript
import express from "express";
import serverless from "serverless-http";
import { router } from '../../src/router';


// https://answers.netlify.com/t/better-sqlite3-causing-500-server-error/127568/2
const app = express();



app.use("/", router);
// handled by netlify.toml redirects
// app.use(express.static('react-app/build/', {
//       setHeaders: (res, path) => {
//     res.set('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
//     res.set('Expires', '0');
//   }
// }));

export const handler = serverless(app);
