## Merge the dictionary
## first dictionary
defaults={"theme":"light",
          "audio":"on"};
user_pref={
    'theme':"dark"
}

defaults.update(user_pref);

print(f"Updated the defaults Dictionary: {defaults}")