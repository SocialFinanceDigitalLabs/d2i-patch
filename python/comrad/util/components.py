def is_component_complete(component: "Component") -> bool:
    """
    Return True if the component is complete. Supports both bound and unbound
    components. Unbound components are always complete.
    """
    try:
        return component.complete
    except AttributeError:
        return True
