from services.supabase import get_supabase


def search_tree(query):

    if not query:
        return []

    supabase = get_supabase()

    result = supabase.rpc(
        "fn_search_tree",
        {
            "search_query": query,
            "result_limit": 25
        }
    ).execute()

    return result.data or []
