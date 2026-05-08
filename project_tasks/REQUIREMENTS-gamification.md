# Requirements: gamification

## Module Overview
- **Name**: Gamification
- **Version**: 1.0
- **Category**: Human Resources
- **Depends**: `mail`
- **License**: LGPL-3

## Description
Gamification process - evaluate and motivate users with goals, challenges, badges, and karma ranking.

## Dependencies

### Internal Dependencies
- `mail` - Mail/messaging for notifications

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `gamification.challenge` | Challenge - set of goals assigned to users |
| `gamification.challenge.line` | Challenge Line - individual goal in challenge |
| `gamification.goal` | Goal - numerical objective to reach |
| `gamification.goal.definition` | Goal Definition - template for goal computation |
| `gamification.badge` | Badge - achievement recognition |
| `gamification.badge.user` | Badge User - granted badge instance |
| `gamification.karma.tracking` | Karma Tracking - karma history |
| `gamification.karma.rank` | Karma Rank - ranking based on karma |
| `res.users` | Extended with karma and badge tracking |

## Views & Security

### Data Files
- `security/gamification_security.xml` - Security rules
- `security/ir.model.access.csv` - Access control
- `data/ir_cron_data.xml` - Scheduled goal/challenge processing
- `data/mail_template_data.xml` - Challenge report templates
- `data/gamification_badge_data.xml` - Badge definitions
- `data/gamification_challenge_data.xml` - Challenge data
- `data/gamification_karma_rank_data.xml` - Karma rank data

### View Files
- `wizard/update_goal.xml`
- `wizard/grant_badge.xml`
- `views/res_users_views.xml`
- `views/gamification_karma_rank_views.xml`
- `views/gamification_karma_tracking_views.xml`
- `views/gamification_badge_views.xml`
- `views/gamification_badge_user_views.xml`
- `views/gamification_goal_views.xml`
- `views/gamification_goal_definition_views.xml`
- `views/gamification_challenge_views.xml`
- `views/gamification_challenge_line_views.xml`
- `views/gamification_menus.xml`

## Key Features
- Goals with numerical objectives
- Challenges with periodicity (once, daily, weekly, monthly, yearly)
- Badges for achievements
- Karma tracking and ranking
- Leaderboard display mode
- Report message frequency settings
- Reward badges for challenge completion
- Top 3 reward rankings
- User domain-based challenge assignment
- Goal reporting and reminders
