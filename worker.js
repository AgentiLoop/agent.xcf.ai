// 301 every clone domain bound to this worker to the canonical agentiloop.ai,
// keeping path and query. workers.dev (preview) and localhost are served as-is.
// Plain-http requests are 301'd to https, and every https response carries HSTS.
const CANONICAL = 'agentiloop.ai';
const HSTS = 'max-age=31536000';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname;
    const local = host === 'localhost' || host === '127.0.0.1';
    if (host !== CANONICAL && !host.endsWith('.workers.dev') && !local) {
      url.protocol = 'https:';
      url.hostname = CANONICAL;
      url.port = '';
      return Response.redirect(url.toString(), 301);
    }
    if (url.protocol === 'http:' && !local) {
      url.protocol = 'https:';
      return Response.redirect(url.toString(), 301);
    }
    const response = await env.ASSETS.fetch(request);
    if (local) return response;
    const out = new Response(response.body, response);
    out.headers.set('Strict-Transport-Security', HSTS);
    return out;
  }
};
