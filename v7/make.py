# Copies Dawn Patrol V7 (~/SurfGame/v7: Extreme Sports Island, more sports) into this site. Adds a proper page header, and keeps Island's
# saves separate from V1-V3, which use the same save names on this site.
SHIM = '''<script>
/* Island shares this site with V1-V3, which save under the same names; keep Island's saves separate. */
(function(){try{var ls=window.localStorage,P='isl:';var w={getItem:function(k){return ls.getItem(P+k)},setItem:function(k,v){ls.setItem(P+k,v)},removeItem:function(k){ls.removeItem(P+k)},clear:function(){},key:function(){return null},get length(){return 0}};Object.defineProperty(window,'localStorage',{value:w,configurable:true});}catch(e){}})();
</script>
'''
src = '/Users/seale/SurfGame/v7/'
s = open(src + 'index.html').read()
open('index.html', 'w').write('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n' + SHIM + s)
s = open(src + 'surf.html').read(); m = '<meta charset="utf-8">\n'; assert m in s
open('surf.html', 'w').write(s.replace(m, m + SHIM, 1))
print('ok')
