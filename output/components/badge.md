# badge

## Metadata
- **Version**: 0.0.1
- **Description**: Visual indicators communicating the status of a component.
- **Category**: components

## Example Sections
1. **Subtle badges**
   - Description: 
2. **Neutral badges**
   - Description: 
3. **Positive badges**
   - Description: 
4. **Warning badges**
   - Description: 
5. **Negative badges**
   - Description: 
6. **Number badges**
   - Description: 

## Examples
### Default subtle badge
- **Section**: Subtle badges
- **URL**: components/badge/subtle-badge-default
- **Tags**: 
```tsx
import { VisaHistoryTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const SubtleBadgeDefault = () => {
  return (
      <Badge badgeType="subtle">
        <VisaHistoryTiny aria-label="history" /> Label
      </Badge>
  );
};

```

### Subtle badge without icon
- **Section**: Subtle badges
- **URL**: components/badge/subtle-badge-without-icon
- **Tags**: 
```tsx
import { Badge} from '@visa/nova-react';

export const SubtleBadgeWithoutIcon = () => {
  return (
      <Badge badgeType="subtle">
         Label
      </Badge>
        );
    };
```

### Subtle badge with indicator
- **Section**: Subtle badges
- **URL**: components/badge/subtle-badge-with-indicator
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const SubtleBadgeWithIndicator = () => {
  return (
      <Badge badgeType="subtle">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Subtle badge without background
- **Section**: Subtle badges
- **URL**: components/badge/subtle-badge-without-background
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const SubtleBadgeWithoutBackground = () => {
  return (
      <Badge badgeType="subtle" clear={true}>
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Default neutral badge
- **Section**: Neutral badges
- **URL**: components/badge/neutral-badge-default
- **Tags**: 
```tsx
import { VisaInformationTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const NeutralBadgeDefault = () => {
  return (
      <Badge badgeType="neutral">
        <VisaInformationTiny aria-label="information" /> Label
      </Badge>
  );
};

```

### Neutral badge without icon
- **Section**: Neutral badges
- **URL**: components/badge/neutral-badge-without-icon
- **Tags**: 
```tsx
import { Badge} from '@visa/nova-react';

export const NeutralBadgeWithoutIcon = () => {
return (
    <Badge badgeType="neutral" aria-label="information">
        Label
    </Badge>
  );
};
```

### Neutral badge with indicator
- **Section**: Neutral badges
- **URL**: components/badge/neutral-badge-with-indicator
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const NeutralBadgeWithIndicator = () => {
  return (
      <Badge badgeType="neutral" aria-label="information">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Neutral badge without background
- **Section**: Neutral badges
- **URL**: components/badge/neutral-badge-without-background
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const NeutralBadgeWithoutBackground = () => {
  return (
      <Badge badgeType="neutral" clear={true} aria-label="information">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Neutral icon badge
- **Section**: Neutral badges
- **URL**: components/badge/neutral-badge-icon
- **Tags**: 
```tsx
import { VisaInformationTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const NeutralBadgeIcon = () => {
  return (
      <Badge badgeType="neutral" badgeVariant="icon">
        <VisaInformationTiny aria-label="information" /> 
      </Badge>
  );
};

```

### Neutral badge icon without background
- **Section**: Neutral badges
- **URL**: components/badge/neutral-badge-icon-without-background
- **Tags**: 
```tsx
import { VisaInformationTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const NeutralBadgeWithIconWithoutBackground = () => {
  return (
      <Badge badgeType="neutral" badgeVariant="icon" clear={true}>
        <VisaInformationTiny aria-label="information" /> 
      </Badge>
  );
};
```

### Default positive badge
- **Section**: Positive badges
- **URL**: components/badge/positive-badge-default
- **Tags**: 
```tsx
import { VisaSuccessTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const PositiveBadgeDefault = () => {
  return (
      <Badge badgeType="stable">
        <VisaSuccessTiny aria-label="success" /> Label
      </Badge>
  );
};

```

### Positive badge without icon
- **Section**: Positive badges
- **URL**: components/badge/positive-badge-without-icon
- **Tags**: 
```tsx
import { Badge} from '@visa/nova-react';

export const PositiveBadgeWithoutIcon = () => {
return (
    <Badge badgeType="stable" aria-label="success">
        Label
    </Badge>
  );
};
```

### Positive badge with indicator
- **Section**: Positive badges
- **URL**: components/badge/positive-badge-with-indicator
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const PositiveBadgeWithIndicator = () => {
  return (
      <Badge badgeType="stable" aria-label="success">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Positive badge without background
- **Section**: Positive badges
- **URL**: components/badge/positive-badge-without-background
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const PositiveBadgeWithoutBackground = () => {
  return (
      <Badge badgeType="stable" clear={true} aria-label="success">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Positive icon badge with background
- **Section**: Positive badges
- **URL**: components/badge/positive-badge-icon
- **Tags**: 
```tsx
import { VisaCheckmarkTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const PositiveBadgeIcon = () => {
  return (
      <Badge badgeType="stable" badgeVariant="icon">
        <VisaCheckmarkTiny aria-label="success" /> 
      </Badge>
  );
};

```

### Positive icon badge without background
- **Section**: Positive badges
- **URL**: components/badge/positive-badge-icon-without-background
- **Tags**: 
```tsx
import { VisaCheckmarkTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const PositiveBadgeWithIconWithoutBackground = () => {
  return (
      <Badge badgeType="stable" badgeVariant="icon" clear={true}>
        <VisaCheckmarkTiny aria-label="success" /> 
      </Badge>
  );
};
```

### Default warning badge
- **Section**: Warning badges
- **URL**: components/badge/warning-badge-default
- **Tags**: 
```tsx
import { VisaWarningTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const WarningBadgeDefault = () => {
  return (
      <Badge badgeType="warning">
        <VisaWarningTiny aria-label="warning" /> Label
      </Badge>
  );
};

```

### Warning badge without icon
- **Section**: Warning badges
- **URL**: components/badge/warning-badge-without-icon
- **Tags**: 
```tsx
import { Badge} from '@visa/nova-react';

export const WarningBadgeWithoutIcon = () => {
return (
    <Badge badgeType="warning" aria-label="warning">
        Label
    </Badge>
  );
};
```

### Warning badge with indicator
- **Section**: Warning badges
- **URL**: components/badge/warning-badge-with-indicator
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const WarningBadgeWithIndicator = () => {
  return (
      <Badge badgeType="warning" aria-label="warning">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Warning badge without background
- **Section**: Warning badges
- **URL**: components/badge/warning-badge-without-background
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const WarningBadgeWithoutBackground = () => {
  return (
      <Badge badgeType="warning" clear={true} aria-label="warning">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Warning icon badge with background
- **Section**: Warning badges
- **URL**: components/badge/warning-badge-icon
- **Tags**: 
```tsx
import { VisaWarningTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const WarningBadgeIcon = () => {
  return (
      <Badge badgeType="warning" badgeVariant="icon">
        <VisaWarningTiny aria-label="warning" /> 
      </Badge>
  );
};

```

### Warning icon badge without background
- **Section**: Warning badges
- **URL**: components/badge/warning-badge-icon-without-background
- **Tags**: 
```tsx
import { VisaWarningTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const WarningBadgeWithIconWithoutBackground = () => {
  return (
      <Badge badgeType="warning" badgeVariant="icon" clear={true}>
        <VisaWarningTiny aria-label="warning" /> 
      </Badge>
  );
};
```

### Default negative badge
- **Section**: Negative badges
- **URL**: components/badge/negative-badge-default
- **Tags**: 
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const NegativeBadgeDefault = () => {
  return (
      <Badge badgeType="critical">
        <VisaErrorTiny aria-label="error" /> Label
      </Badge>
  );
};

```

### Negative badge without icon
- **Section**: Negative badges
- **URL**: components/badge/negative-badge-without-icon
- **Tags**: 
```tsx
import { Badge} from '@visa/nova-react';

export const NegativeBadgeWithoutIcon = () => {
return (
    <Badge badgeType="critical" aria-label="error">
        Label
    </Badge>
  );
};
```

### Negative badge with indicator
- **Section**: Negative badges
- **URL**: components/badge/negative-badge-with-indicator
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const NegativeBadgeWithIndicator = () => {
  return (
      <Badge badgeType="critical" aria-label="error">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Negative badge without background
- **Section**: Negative badges
- **URL**: components/badge/negative-badge-without-background
- **Tags**: 
```tsx
import { Badge, BadgeEllipse } from '@visa/nova-react';

export const NegativeBadgeWithoutBackground = () => {
  return (
      <Badge badgeType="critical" clear={true} aria-label="error">
        <BadgeEllipse />
        Label
      </Badge>
  );
};

```

### Negative icon badge with background
- **Section**: Negative badges
- **URL**: components/badge/negative-badge-icon
- **Tags**: 
```tsx
import { VisaErrorAltTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const NegativeBadgeIcon = () => {
  return (
      <Badge badgeType="critical" badgeVariant="icon">
        <VisaErrorAltTiny aria-label="error" /> 
      </Badge>
  );
};

```

### Negative icon badge without background
- **Section**: Negative badges
- **URL**: components/badge/negative-badge-icon-without-background
- **Tags**: 
```tsx
import { VisaErrorAltTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const NegativeBadgeWithIconWithoutBackground = () => {
  return (
      <Badge badgeType="critical" badgeVariant="icon" clear={true}>
        <VisaErrorAltTiny aria-label="error" /> 
      </Badge>
  );
};
```

### Short number badge with background
- **Section**: Number badges
- **URL**: components/badge/badge-number-default
- **Tags**: 
```tsx
import { Badge } from '@visa/nova-react';

export const BadgeNumberDefault = () => {
  return <Badge badgeType="critical" badgeVariant="number">3</Badge>;
};

```

### Short number badge without background
- **Section**: Number badges
- **URL**: components/badge/badge-number-without-background
- **Tags**: 
```tsx
import { Badge } from '@visa/nova-react';

export const BadgeNumberWithoutBackground = () => {
  return <Badge badgeType="critical" badgeVariant="number" clear={true}>3</Badge>;
};
```

### Long number badge
- **Section**: Number badges
- **URL**: components/badge/badge-number-long
- **Tags**: 
```tsx
import { Badge } from '@visa/nova-react';

export const BadgeNumberLong = () => {
  return <Badge badgeType="critical" badgeVariant="number">12345</Badge>;
};

```

## Property Sections
### Badge
- **Selector**: <Badge />
- **Description**: Visual indicators communicating the status of a component.

## Properties
### active
- **Section**: Badge
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Active style

### badgeType
- **Section**: Badge
- **Type**: "subtle" , "critical" , "neutral" , "stable" , "warning"
- **Default**: 
- **Required**: false
- **Description**: Type of Badge

### badgeVariant
- **Section**: Badge
- **Type**: "number" , "icon"
- **Default**: 
- **Required**: false
- **Description**: Variant of Badge

### clear
- **Section**: Badge
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Clear background

### ref
- **Section**: Badge
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Badge
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

