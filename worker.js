// 301 every clone domain bound to this worker to the canonical agentiloop.ai,
// keeping path and query. workers.dev (preview) and localhost are served as-is.
const CANONICAL = 'agentiloop.ai';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname;
    if (host !== CANONICAL && !host.endsWith('.workers.dev') && host !== 'localhost' && host !== '127.0.0.1') {
      url.protocol = 'https:';
      url.hostname = CANONICAL;
      url.port = '';
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  }
};
