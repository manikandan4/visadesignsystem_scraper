# anchor-link-menu

## Metadata
- **Version**: 0.0.1
- **Description**: Menu of links that navigate to sections within the current page.
- **Category**: components

## Example Sections
1. **Default anchor link menus**
   - Description: 

## Examples
### Default anchor link menu
- **Section**: Default anchor link menus
- **URL**: components/anchor-link-menu/default-anchor-link-menu
- **Tags**: 
```tsx
import { AnchorLinkMenu, AnchorLinkMenuHeader, Link, Typography } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-anchor-link-menu';

export const DefaultAnchorLinkMenu = () => {
  return (
    <AnchorLinkMenu aria-labelledby={`${id}-header`}>
      <section>
        <AnchorLinkMenuHeader>
          <Typography id={`${id}-header`} tag="h2" variant="overline">
            Section title
          </Typography>
        </AnchorLinkMenuHeader>
        <ul>
          <li>
            <Link aria-current="true" href="./anchor-link-menu">
              L1 label 1
            </Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 2</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 3</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 4</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 5</Link>
          </li>
        </ul>
      </section>
    </AnchorLinkMenu>
  );
};

```

### Anchor link menu without section title
- **Section**: Default anchor link menus
- **URL**: components/anchor-link-menu/no-title-anchor-link-menu
- **Tags**: 
```tsx
import { AnchorLinkMenu, Link } from '@visa/nova-react';

export const NoTitleAnchorLinkMenu = () => {
  return (
    <AnchorLinkMenu aria-label="Section title">
      <section>
        <ul>
          <li>
            <Link aria-current="true" href="./anchor-link-menu">
              L1 label 1
            </Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 2</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 3</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 4</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 5</Link>
          </li>
        </ul>
      </section>
    </AnchorLinkMenu>
  );
};

```

### Anchor link menu with nested items
- **Section**: Default anchor link menus
- **URL**: components/anchor-link-menu/nested-anchor-link-menu
- **Tags**: 
```tsx
import { AnchorLinkMenu, AnchorLinkMenuHeader, Link, Typography } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nested-anchor-link-menu';

export const NestedAnchorLinkMenu = () => {
  return (
    <AnchorLinkMenu aria-labelledby={`${id}-header`}>
      <section>
        <AnchorLinkMenuHeader>
          <Typography id={`${id}-header`} tag="h2" variant="overline">
            Section title
          </Typography>
        </AnchorLinkMenuHeader>
        <ul>
          <li>
            <Link aria-current="true" href="./anchor-link-menu">
              L1 label 1
            </Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 2</Link>
            <ul>
              <li>
                <Link href="./anchor-link-menu">L2 label 1</Link>
              </li>
              <li>
                <Link href="./anchor-link-menu">L2 label 2</Link>
              </li>
            </ul>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 3</Link>
          </li>
        </ul>
      </section>
    </AnchorLinkMenu>
  );
};

```

### Right to left anchor link menu
- **Section**: Default anchor link menus
- **URL**: components/anchor-link-menu/direction-rtl-anchor-link-menu
- **Tags**: 
```tsx
import { AnchorLinkMenu, AnchorLinkMenuHeader, Link, Typography } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'rtl-anchor-link-menu';

export const DirectionRTLAnchorLinkMenu = () => {
  return (
    <AnchorLinkMenu aria-labelledby={`${id}-header`} dir="rtl">
      <section>
        <AnchorLinkMenuHeader>
          <Typography id={`${id}-header`} tag="h2" variant="overline">
            Section title
          </Typography>
        </AnchorLinkMenuHeader>
        <ul>
          <li>
            <Link aria-current="true" href="./anchor-link-menu">
              L1 label 1
            </Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 2</Link>
            <ul>
              <li>
                <Link href="./anchor-link-menu">L2 label 1</Link>
              </li>
              <li>
                <Link href="./anchor-link-menu">L2 label 2</Link>
              </li>
            </ul>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 3</Link>
          </li>
        </ul>
      </section>
    </AnchorLinkMenu>
  );
};

```

## Property Sections
### AnchorLinkMenu
- **Selector**: <AnchorLinkMenu />
- **Description**: Menu of links that navigate to sections within the current page.

### AnchorLinkMenuHeader
- **Selector**: <AnchorLinkMenuHeader />
- **Description**: Component containing the header of the anchor link menu.

## Properties
### ref
- **Section**: AnchorLinkMenu
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: AnchorLinkMenu
- **Type**: ElementType
- **Default**: aside
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: AnchorLinkMenuHeader
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: AnchorLinkMenuHeader
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

