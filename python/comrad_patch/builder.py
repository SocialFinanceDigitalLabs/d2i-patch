from comrad import server

from .util.files import load_json, load_yaml


def load_manifest(file_path: str) -> dict:
    if file_path.endswith(".json"):
        return load_json(file_path)
    return load_yaml(file_path)


def parse_component():
    """Convert patch to comrad component"""
    # TODO
    pass


def builder(file_path: str):
    server_pages: list[server.Page] = []
    manifest = load_manifest(file_path)
    for page in manifest["pages"]:
        components: list[server.Component] = []
        for component in page["components"]:
            components.append(
                server.Component(type_name=component["type"])
            )  # TODO - properly convert components
        container_component = server.ContainerComponent(components=components)
        view = server.ComponentView(component=container_component)
        controller = server.DefaultController(
            view=view, next=page["controller"]["next"] if page["controller"] else None
        )
        server_page = server.MVCPage(
            controller=controller, name=page["name"], view=view
        )
        server_pages.append(server_page)

    if default_page_name := manifest["pages"][0]["name"]:
        router = server.DefaultRouter(
            pages=server_pages, default_page_name=default_page_name
        )
    else:
        router = server.DefaultRouter(pages=server_pages)

    return server.Application(router=router)
