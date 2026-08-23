from services.supabase import get_supabase


def get_root_nodes():

    supabase = get_supabase()

    result = (
        supabase
        .table("nodes")
        .select("*")
        .is_("parent_id", "null")
        .order("sort_order")
        .execute()
    )

    return result.data or []


def get_children(node_id):

    supabase = get_supabase()

    result = (
        supabase
        .table("nodes")
        .select("*")
        .eq("parent_id", node_id)
        .order("sort_order")
        .execute()
    )

    return result.data or []


def get_unit_links(node_id):

    supabase = get_supabase()

    result = supabase.rpc(
        "fn_get_unit_links",
        {
            "p_node_id": node_id
        }
    ).execute()

    return result.data or []
