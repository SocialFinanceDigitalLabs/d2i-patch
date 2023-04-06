def is_component_complete(
    component: "comrad.server.Component", unbound_value=True
) -> bool:
    """
    Return True if the component is complete. Supports both bound and unbound
    components. Unbound components are considered `unbound_value` (defaults to True).
    """
    try:
        return component.complete
    except AttributeError:
        return unbound_value
