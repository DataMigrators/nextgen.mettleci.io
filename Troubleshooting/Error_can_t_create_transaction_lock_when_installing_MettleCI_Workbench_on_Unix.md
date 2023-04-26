# Error "can't create transaction lock" when installing MettleCI Workbench on Unix

# Symptom

You receive a `can't create transaction lock` error when attempting to
install the Workbench on a Unix environment using `rpm`:

``` bash
$> rpm -U dm-mettleci-workbench-1.0-1405.noarch.rpm
error: can't create transaction lock on /var/lib/rpm/.rpm.lock (Permission denied)
```

# Cause

You aren’t running the Workbench `rpm` installation as the `root` user,
or as a user with `root` privileges.

# Solution

Run the Workbench `rpm` installation as the `root` user!
<img src="images/icons/emoticons/wink.png"
class="emoticon emoticon-wink" data-emoji-id="1f609"
data-emoji-shortname=":wink:" data-emoji-fallback="😉"
data-emoticon-name="wink" width="16" height="16" alt="(wink)" />
