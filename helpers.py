import json
from datetime import datetime, timedelta, timezone
from urllib.parse import unquote


def convert_datetime_str_to_utc(datetime_str):
    decimal_index = datetime_str.find(".")
    if decimal_index != -1:
        # Ensure only 3 digits after the decimal point for milliseconds
        datetime_str = datetime_str[: decimal_index + 4]

    return datetime.fromisoformat(datetime_str).replace(tzinfo=timezone.utc)


def format_duration(seconds):
    message = ""
    duration_td = timedelta(seconds=seconds)
    days, day_remainder = divmod(duration_td.total_seconds(), 86400)
    hours, remainder = divmod(day_remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days:
        message = f"{int(days)} hari "

    if hours:
        message = message + f"{int(hours)} jam "

    if minutes:
        message = message + f"{int(minutes)} menit "

    if seconds:
        message = message + f"{int(seconds)} detik"
    return message.strip()


def remove_query_id_from_tg_web_data(tg_web_data):
    data_to_be_splitted = tg_web_data
    splitted_original_data = data_to_be_splitted.split("&")
    return "&".join(splitted_original_data[1:])


def mapping_role_color(role):
    if role == "admin":
        role = f"<lg>{role}</lg>"
    elif role == "premium":
        role = f"<lc>{role}</lc>"

    return role


def decode_query_id(query_id):
    query_string = query_id
    if 'tgWebAppData' in query_id:
        query_string = unquote(string=query_id.split("tgWebAppData=", maxsplit=1)[1].split("&tgWebAppVersion", maxsplit=1)[0])
    parameters = query_string.split("&")
    decoded_pairs = [(param.split("=")[0], unquote(param.split("=")[1])) for param in parameters]
    result = dict()
    for key, value in decoded_pairs:
        result[key] = value

    reassign(result)
    return result


def reassign(d):
    """
    check if you have a dict after using literal_eval and reassign
    """
    for k, v in d.items():
        if v[0] in {"{", "["}:
            try:
                evald = json.loads(v)
                if isinstance(evald, dict):
                    d[k] = evald
            except ValueError as err:
                pass


async def get_query_ids():
    temp_lines = []
    with open("query_ids.txt", "r") as file:
        temp_lines = file.readlines()

    lines = [line.strip() for line in temp_lines]
    return lines


def get_tele_user_obj_from_query_id(query_id):
    # formatted_query_id = unquote(string=query_id)
    query_obj = decode_query_id(query_id)
    tele_user_obj = query_obj.get("user", {})
    return tele_user_obj


def populate_not_started_tasks(tasks: list):
    not_started_tasks = []
    for task in tasks:
        if task.get("title") == "Promo":
            continue
        sub_tasks = task.get("tasks")
        for sub_task in sub_tasks:
            if (
                sub_task.get("status") == "NOT_STARTED"
                and sub_task.get("socialSubscription", {}).get("openInTelegram") is not True
                and sub_task.get("isHidden") is not True
            ):
                temp_task = {
                    "task_id": sub_task.get("id"),
                    "task_title": sub_task.get("title"),
                }
                not_started_tasks.append(temp_task)
    return not_started_tasks


def populate_not_claimed_tasks(tasks: list):
    not_claimed_tasks = []
    for task in tasks:
        if task.get("title") == "Promo":
            continue
        sub_tasks = task.get("tasks")
        for sub_task in sub_tasks:
            if sub_task.get("status") == "READY_FOR_CLAIM":
                temp_task = {
                    "task_id": sub_task.get("id"),
                    "task_title": sub_task.get("title"),
                    "task_reward": sub_task.get("reward"),
                }
                not_claimed_tasks.append(temp_task)
    return not_claimed_tasks
