import json

import requests
from django.shortcuts import render


# Create your views here.

def index(request):
    if request.method == "GET":
        text = "https://sleepy-plain.herokuapp.com/?code=AQBvCYrdMMYFYRSW1eQiLb4B8d8-KwtNc420obkPspDYmMHDJf0hR5_vzJYpfmcn3ZLCNXkm8iJ45ah8l7ILO1LLaY-4oErw58KRhsTLlCbPZjhw6vfK3JdUoWuhNSaR7_LHxeWva57J2FxhofcHeRORH-D_rCUWPIlRHEyh4BJV_5k7rKKBKjzhGf-xkY9Ve2IR_MaMYHdZE0oBnN1oBe2unsxz2D9StapLNqhIxIA_6A#_"
        return render(request, "index.html")


def code(request):
    if request.method == "GET":
        print(absolute(request)["ABSOLUTE_ROOT"])
        print(absolute(request)["ABSOLUTE_ROOT_SLASH"])
        print(absolute(request)["ABSOLUTE_ROOT"])
        code = request.GET.get("code", None)
        if code is not None:
            code = strip_end(code, "#_")
        r = requests.get("https://www.instagram.com/" + "hongmingu" + "/?__a=1")
        get_text = json.loads(r.text)
        follower_count = get_text["graphql"]["user"]["edge_followed_by"]["count"]
        following_count = get_text["graphql"]["user"]["edge_follow"]["count"]
        print(following_count)
        redirect_uri = "https://www.neontab.com/"
        grant_type = "authorization_code"
        client_id = "453531205633119"
        client_secret = "9d215ffa8ed163c081d84c25f2d2e85a"

        response = requests.post('https://api.instagram.com/oauth/access_token', data={'client_id': client_id,
                                                                                       'client_secret': client_secret,
                                                                                       'grant_type': grant_type,
                                                                                       'redirect_uri': redirect_uri,
                                                                                       'code': code,
                                                                                       })

        json_response = json.loads(response.text)
        print(json_response)
        access_token = json_response["access_token"]
        user_id = json_response["user_id"]

        response_me = requests.get(
            "https://graph.instagram.com/" + str(user_id) + "?fields=id,username&access_token=" + access_token)
        print(response_me.content)

        print(response_me.text)
        json_2 = json.loads(response_me.text)

        instagram_id = json_2["id"]
        instagram_username = json_2["username"]

        print("instagramid: " + instagram_id)
        print("instagramusername: " + instagram_username)
        print(response_me.url)
        return render(request, "code.html", {"response_text": response.text, "response_me": response_me})


import traceback


def instagram_some(request, name):
    if request.method == "GET":
        if name == "redirect":

            response_all = None
            response_info = None
            response_third = None
            response_post = None
            try:

                code = request.GET.get("code", None)
                if code is not None:
                    code = strip_end(code, "#_")
                else:
                    return render(request, "404.html")

                insta_all = "https://www.instagram.com/" + "hongmingu" + "/?__a=1"
                response_all = requests.get(insta_all)
                print(response_all.text)
                get_text = json.loads(response_all.text)
                follower_count = get_text["graphql"]["user"]["edge_followed_by"]["count"]
                following_count = get_text["graphql"]["user"]["edge_follow"]["count"]
                instagram_id = get_text["graphql"]["user"]["id"]
                instagram_username = get_text["graphql"]["user"]["username"]

                # redirect_uri = absolute(request)['ABSOLUTE_ROOT'] + reverse("baseapp:instagram_some", kwargs={"name": "redirect"})
                redirect_uri = "https://sleepy-plain.herokuapp.com/instagram/redirect/"
                grant_type = "authorization_code"
                fb_client_id = "453531205633119"
                fb_client_secret = "9d215ffa8ed163c081d84c25f2d2e85a"
                fb_insta_api_url = "https://api.instagram.com/oauth/access_token"

                response_post = requests.post(fb_insta_api_url, data={'client_id': fb_client_id,
                                                                      'client_secret': fb_client_secret,
                                                                      'grant_type': grant_type,
                                                                      'redirect_uri': redirect_uri,
                                                                      'code': code,
                                                                      })

                json_response = json.loads(response_post.text)
                print(response_post.text)
                access_token = json_response["access_token"]
                user_id = json_response["user_id"]

                response_info = requests.get(
                    "https://graph.instagram.com/" + str(user_id) + "?fields=id,username&access_token=" + access_token)

                json_info = json.loads(response_info.text)

                instagram_id = json_info["id"]
                instagram_username = json_info["username"]

                response_third = requests.get(
                    "https://www.instagram.com/" + str(instagram_username).strip() + "/?__a=1")
                get_text = json.loads(response_third.text)
                follower_count = get_text["graphql"]["user"]["edge_followed_by"]["count"]
                following_count = get_text["graphql"]["user"]["edge_follow"]["count"]
                # instagram_id = get_text["graphql"]["user"]["id"]
                # instagram_username = get_text["graphql"]["user"]["username"]



            except Exception as e:
                print(e)
                return render(request, "baseapp/instagram_redirect.html", {
                    "clue": traceback.format_exc() + "/responseall/" + response_all.text + "/responseinfo/" + response_info.text + "/responsethird/" + response_third + "/responsepost/" + response_post})

            # return redirect(reverse('authapp:settings'))
            return render(request, "baseapp/instagram_redirect.html", {"instagram_username": instagram_username})

        elif name == "cancelled":
            return render(request, "baseapp/instagram_cancelled.html")

            # return redirect(reverse('authapp:settings'))
        elif name == "delete":
            return render(request, "baseapp/instagram_delete.html")
            # return redirect(reverse('authapp:settings'))
        elif name == "test":
            fb_client_id = "453531205633119"
            # fb_redirect_uri = absolute(request)['ABSOLUTE_ROOT'] + reverse("baseapp:instagram_some", kwargs={"name": "redirect"})
            fb_redirect_uri = "https://sleepy-plain.herokuapp.com/instagram/redirect/"

            instagram_link = "https://api.instagram.com/oauth/authorize?client_id=" + fb_client_id + "&redirect_uri=" + fb_redirect_uri + "&scope=user_profile&response_type=code"

            return render(request, "baseapp/instagram_test.html", {"instagram_link": instagram_link})
            # return redirect(reverse('authapp:settings'))
        else:
            return render(request, "404.html")



def strip_end(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:len(text) - len(suffix)]


def absolute(request):
    urls = {
        'ABSOLUTE_ROOT': request.build_absolute_uri('/')[:-1].strip("/"),
        'ABSOLUTE_ROOT_SLASH': request.build_absolute_uri('/')[:-1].strip("/") + "/",
        'ABSOLUTE_ROOT_URL': request.build_absolute_uri('/').strip("/"),
    }

    return urls