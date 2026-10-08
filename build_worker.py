import json, os
html = open('index.html', encoding='utf-8').read()
sitemap = open('sitemap.xml', encoding='utf-8').read()
js = """// SpaceWise landing page Worker. Serves ONE path on fuidzy.com and nothing else.
const HTML = %s;
const SITEMAP = %s;
const PATH = "/deep-clean-pc-or-mac-storage";
export default {
  async fetch(request) {
    const url = new URL(request.url);
    const p = url.pathname.replace(/\/+$/, "") || "/";
    const h = { "content-type": "text/html; charset=utf-8", "cache-control": "public, max-age=300", "x-content-type-options": "nosniff", "referrer-policy": "strict-origin-when-cross-origin" };
    if (request.method !== "GET" && request.method !== "HEAD") return new Response("Method not allowed", { status: 405 });
    if (p === PATH) return new Response(request.method === "HEAD" ? null : HTML, { headers: h });
    if (p === PATH + "/sitemap.xml") return new Response(SITEMAP, { headers: { "content-type": "application/xml; charset=utf-8", "cache-control": "public, max-age=3600" } });
    return fetch(request);   // anything else falls through to whatever served it before
  },
};
""" % (json.dumps(html), json.dumps(sitemap))
os.makedirs('worker', exist_ok=True)
open('worker/worker.js', 'w', encoding='utf-8').write(js)
print('worker.js bytes:', len(js))
