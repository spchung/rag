import { Application, Router } from "https://deno.land/x/oak@v17.1.3/mod.ts";

const port = 8080;
const app = new Application();

app.use(async (ctx, next) => {
  await next();
  console.log(`HTTP ${ctx.request.method} on ${ctx.request.url}`);
});

app.addEventListener('listen', () => {
  console.log(`Listening on localhost:${port}`);
});

const router = new Router();

router
  .get('/', (ctx) => {
    ctx.response.body = 'Hello Denossss';
  })
  .get('/about', (ctx) => {
    ctx.response.body = 'About Denossss';
  })
;

app.use(router.routes());
app.use(router.allowedMethods());

await app.listen({ port });