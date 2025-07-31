from fastapp import FastAppRouter, Request

router = FastAppRouter()


@router.get("/")
async def dynamic_page(request: Request, name: str):
    return router.render({"name": name})  # no template name needed
