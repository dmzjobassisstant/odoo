# im_livechat — Requirements

## Module Overview
- **Name**: Live Chat
- **Version**: 1.0
- **Category**: Website/Live Chat
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Application**: True

## Dependencies
- `mail`
- `rating`
- `digest`
- `utm`

## Core Functionality
Allows dropping instant messaging widgets on web pages to communicate with website visitors. Dispatches visitor requests among live chat operators. Includes chatbot automation.

## Key Models
- `im_livechat.channel` — Livechat channel (name, button text, default message, colors, max sessions, rules)
- `discuss.channel` — Extended with livechat support
- `im_livechat.channel.rule` — Channel rules
- `chatbot.script` — Chatbot automation scripts
- `chatbot.script.step` — Chatbot conversation steps
- `chatbot.script.answer` — Chatbot answer options
- `im_livechat.expertise` — Operator expertise areas
- `im_livechat.conversation.tag` — Conversation tagging
- `discuss.channel.member` — Extended for livechat
- `rating.rating` — Extended for livechat ratings
- `res.partner` — Extended for livechat
- `res.users` — Extended for livechat
- `res.users.settings` — User settings for livechat
- `discuss.call.history` — Call history
- `discuss.channel.rtc.session` — WebRTC sessions

## Key Features
- Embeddable livechat widget (external/frontend)
- Chatbot automation with scripted conversations
- Operator assignment and load balancing
- Session capacity management
- Call blocking during active calls
- Review links for positive feedback
- Session history and tagging
- Website visitor tracking via UTM
- Rating and satisfaction tracking
- Digest integration for statistics

## Data Files
- `security/im_livechat_channel_security.xml`
- `security/ir.model.access.csv`
- `data/mail_templates.xml`
- `data/im_livechat_channel_data.xml`
- `data/im_livechat_chatbot_data.xml`
- `data/digest_data.xml`
- Multiple views (chatbot, channel, discuss, partner, user, digest, reports)

## Demo Data
- Demo channel, chatbot scripts, chatbot sessions, chat sessions

## Assets (Multiple Custom Bundles)

### `im_livechat.assets_embed_core`
- Core embed functionality (mail models, discuss core, rating, common)

### `im_livechat.assets_embed_external`
- Full external embed with bootstrap, web helpers

### `im_livechat.assets_embed_cors`
- CORS-specific embed assets

### `im_livechat.qunit_embed_suite`
- Embed unit tests

### `im_livechat.embed_assets_unit_tests`
- Embed integration tests

### `im_livechat.assets_livechat_support_tours`
- Support bot tour system

### `mail.assets_public`
- Public assets for livechat

## WebSocket
- Real-time updates via `bus` module
- WebSocket for livechat notifications

## Security
- Channel-specific security rules (`im_livechat_channel_security.xml`)
- Access control via `ir.model.access.csv`
