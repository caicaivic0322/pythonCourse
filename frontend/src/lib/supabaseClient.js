const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;
const sessionKey = 'supabase_auth_session';

if (!supabaseUrl || !supabaseAnonKey) {
  throw new Error('Missing Supabase environment variables');
}

function readSession() {
  const raw = localStorage.getItem(sessionKey);
  return raw ? JSON.parse(raw) : null;
}

function writeSession(session) {
  localStorage.setItem(sessionKey, JSON.stringify(session));
}

function removeSession() {
  localStorage.removeItem(sessionKey);
}

export function getAccessToken() {
  return readSession()?.access_token || null;
}

export function setSession(session) {
  writeSession(session);
}

export function clearSession() {
  removeSession();
}

export async function authRequest(path, options = {}) {
  const response = await fetch(`${supabaseUrl}/auth/v1${path}`, {
    ...options,
    headers: {
      apikey: supabaseAnonKey,
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(payload?.msg || payload?.error_description || payload?.message || 'Auth request failed');
  }
  return payload;
}

export async function restRequest(path, options = {}) {
  const token = getAccessToken();
  const response = await fetch(`${supabaseUrl}/rest/v1${path}`, {
    ...options,
    headers: {
      apikey: supabaseAnonKey,
      Authorization: token ? `Bearer ${token}` : undefined,
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });
  const payload = await response.json().catch(() => null);
  if (!response.ok) {
    throw new Error(payload?.message || 'Database request failed');
  }
  return payload;
}
