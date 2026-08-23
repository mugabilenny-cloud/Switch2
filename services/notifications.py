from services.supabase import get_supabase
from services.device import get_device_token


def get_notifications(limit=5):

    supabase = get_supabase()

    device_token = get_device_token()

    result = supabase.rpc(
        "fn_get_notifications_for_device",
        {
            "p_device_token": device_token,
            "p_limit": limit
        }
    ).execute()

    return result.data or []


def mark_seen(
    notification_id,
    dismissed=False
):

    supabase = get_supabase()

    device_token = get_device_token()

    return supabase.rpc(
        "fn_mark_notification_seen",
        {
            "p_notification_id": notification_id,
            "p_device_token": device_token,
            "p_dismissed": dismissed
        }
    ).execute()
