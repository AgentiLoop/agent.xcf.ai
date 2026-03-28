export async function onRequestPost(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };

  try {
    const body = await context.request.json();
    const { name, email, message } = body;

    if (!name || !email || !message) {
      return new Response(JSON.stringify({ error: 'All fields are required.' }), {
        status: 400,
        headers,
      });
    }

    // Basic email validation
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return new Response(JSON.stringify({ error: 'Invalid email address.' }), {
        status: 400,
        headers,
      });
    }

    const send = await fetch('https://api.mailchannels.net/tx/v1/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        personalizations: [
          {
            to: [{ email: 'starplayr@icloud.com', name: 'Agent! Contact' }],
          },
        ],
        from: {
          email: 'noreply@xcf.ai',
          name: 'Agent! Website',
        },
        reply_to: {
          email: email,
          name: name,
        },
        subject: 'Agent! Contact: ' + name,
        content: [
          {
            type: 'text/plain',
            value: 'Name: ' + name + '\nEmail: ' + email + '\n\n' + message,
          },
        ],
      }),
    });

    if (send.status === 202 || send.ok) {
      return new Response(JSON.stringify({ success: true }), {
        status: 200,
        headers,
      });
    }

    const err = await send.text();
    console.error('MailChannels error:', send.status, err);
    return new Response(JSON.stringify({ error: 'Failed to send email.' }), {
      status: 500,
      headers,
    });
  } catch (e) {
    console.error('Contact form error:', e);
    return new Response(JSON.stringify({ error: 'Server error.' }), {
      status: 500,
      headers,
    });
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
