# panel

## Metadata
- **Version**: 0.0.1
- **Description**: Collapsible or persistent containers used to present supplementary information.
- **Category**: components

## Example Sections
1. **Default panels**
   - Description: 
2. **Expandable panels**
   - Description: 
3. **Tabbed panels**
   - Description: 

## Examples
### Modal panel
- **Section**: Default panels
- **URL**: components/panel/modal-panel
- **Tags**: 
```tsx
import { VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'modal-panel-default';

export const ModalPanel = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open modal panel</Button>
      <Panel
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        aria-modal="true"
        id={id}
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
        ref={ref}
        tag="dialog"
      >
        <PanelContent>
          <Utility element={<PanelHeader />} vFlex vFlexRow vJustifyContent="between" vGap={4}>
            <Typography id={`${id}-title`} tag="h2" variant="headline-3">
              Panel title
            </Typography>
            <Button
              aria-label="Close panel"
              buttonSize="small"
              className="-v-mt-3 -v-mr-8"
              colorScheme="tertiary"
              iconButton
              onClick={() => ref.current?.close()}
              subtle
            >
              <VisaCloseTiny />
            </Button>
          </Utility>
          <PanelBody>
            <Typography id={`${id}-description`} tag="h3" variant="subtitle-2">
              Panel subtitle
            </Typography>
            <Typography>
              This is required text that can be used to describe the panel title and subtitle in more detail.
            </Typography>
          </PanelBody>
        </PanelContent>
      </Panel>
    </>
  );
};

```

### Default responsive panel
- **Section**: Default panels
- **URL**: components/panel/default-panel
- **Tags**: 
```tsx
import { VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  Typography,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';

export const DefaultPanel = () => {
  return (
    <Utility vFlex>
      <UtilityFragment vMarginLeft="auto">
        <Panel style={{ minInlineSize: 'initial' }}>
          <PanelContent>
            <Utility element={<PanelHeader />} vFlex vFlexRow vGap={4} vJustifyContent="between">
              <Typography tag="h2" variant="headline-3">
                Panel title
              </Typography>
              <Button
                aria-label="Close panel"
                buttonSize="small"
                className="-v-mt-3 -v-mr-8"
                colorScheme="tertiary"
                iconButton
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </Utility>
            <PanelBody>
              <Typography tag="h3" variant="subtitle-2">
                Panel subtitle
              </Typography>
              <Typography>
                This is required text that can be used to describe the panel title and subtitle in more detail.
              </Typography>
            </PanelBody>
          </PanelContent>
        </Panel>
      </UtilityFragment>
    </Utility>
  );
};

```

### Modal expandable panel
- **Section**: Expandable panels
- **URL**: components/panel/expandable-panel
- **Tags**: 
```tsx
import { VisaMediaFastForwardTiny, VisaMediaRewindTiny } from '@visa/nova-icons-react';
import {
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  PanelToggle,
  Typography,
  useFocusTrap,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';

export const ModalExpandablePanel = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <Utility vFlex>
      <UtilityFragment vMarginLeft="auto">
        <PanelToggle
          aria-expanded="false"
          aria-label="Open panel"
          buttonSize="large"
          iconButton
          iconTwoColor
          onClick={() => ref.current?.showModal()}
        >
          <VisaMediaRewindTiny rtl />
        </PanelToggle>
      </UtilityFragment>

      <UtilityFragment vMarginLeft="auto">
        <Panel
          expandable
          onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
          ref={ref}
          style={{ height: 400 }}
          tag="dialog"
        >
          <PanelToggle
            aria-expanded="true"
            aria-label="Close panel"
            buttonSize="large"
            iconButton
            iconTwoColor
            onClick={() => ref.current?.close()}
          >
            <VisaMediaFastForwardTiny rtl />
          </PanelToggle>

          <PanelContent>
            <PanelHeader>
              <Typography tag="h2" variant="headline-3">
                Panel title
              </Typography>
            </PanelHeader>
            <PanelBody>
              <Typography tag="h3" variant="subtitle-2">
                Panel subtitle
              </Typography>
              <Typography>
                This is required text that can be used to describe the panel title and subtitle in more detail.
              </Typography>
            </PanelBody>
          </PanelContent>
        </Panel>
      </UtilityFragment>
    </Utility>
  );
};

```

### Responsive expanded panel
- **Section**: Expandable panels
- **URL**: components/panel/expandable-responsive-panel
- **Tags**: 
```tsx
import { VisaMediaFastForwardTiny, VisaMediaRewindTiny } from '@visa/nova-icons-react';
import {
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  PanelToggle,
  Typography,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { useState } from 'react';

export const ExpandableResponsivePanel = () => {
  const [open, setOpen] = useState(true);

  return (
    <Utility vFlex style={{ minBlockSize: 200 }}>
      <UtilityFragment vMarginLeft="auto">
        <PanelToggle
          aria-expanded={open}
          aria-label={open ? 'Close panel' : 'Open panel'}
          buttonSize="large"
          iconButton
          iconTwoColor
          onClick={() => setOpen(open ? false : true)}
        >
          {open ? <VisaMediaFastForwardTiny rtl /> : <VisaMediaRewindTiny rtl />}
        </PanelToggle>
      </UtilityFragment>

      {open && (
        <Panel expandable style={{ minInlineSize: 'initial' }}>
          <PanelContent>
            <PanelHeader>
              <Typography tag="h2" variant="headline-3">
                Panel title
              </Typography>
            </PanelHeader>
            <PanelBody>
              <Typography tag="h3" variant="subtitle-2">
                Panel subtitle
              </Typography>
              <Typography>
                This is required text that can be used to describe the panel title and subtitle in more detail.
              </Typography>
            </PanelBody>
          </PanelContent>
        </Panel>
      )}
    </Utility>
  );
};

```

### Modal expandable panel with secondary button
- **Section**: Expandable panels
- **URL**: components/panel/expandable-panel-secondary
- **Tags**: 
```tsx
import { VisaMediaFastForwardTiny, VisaMediaRewindTiny } from '@visa/nova-icons-react';
import {
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  PanelToggle,
  Typography,
  useFocusTrap,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';

export const SecondaryModalExpandablePanel = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <Utility vFlex>
      <UtilityFragment vMarginLeft="auto">
        <PanelToggle
          aria-expanded={false}
          aria-label="Open panel"
          buttonSize="large"
          colorScheme="secondary"
          iconButton
          onClick={() => ref.current?.showModal()}
        >
          <VisaMediaRewindTiny rtl />
        </PanelToggle>
      </UtilityFragment>

      <UtilityFragment vMarginLeft="auto">
        <Panel
          expandable
          onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
          ref={ref}
          style={{ height: 400 }}
          tag="dialog"
        >
          <PanelToggle
            aria-expanded="true"
            aria-label="Close panel"
            buttonSize="large"
            colorScheme="secondary"
            iconButton
            onClick={() => ref.current?.close()}
          >
            <VisaMediaFastForwardTiny rtl />
          </PanelToggle>

          <PanelContent>
            <PanelHeader>
              <Typography tag="h2" variant="headline-3">
                Panel title
              </Typography>
            </PanelHeader>
            <PanelBody>
              <Typography tag="h3" variant="subtitle-2">
                Panel subtitle
              </Typography>
              <Typography>
                This is required text that can be used to describe the panel title and subtitle in more detail.
              </Typography>
            </PanelBody>
          </PanelContent>
        </Panel>
      </UtilityFragment>
    </Utility>
  );
};

```

### Modal expandable panel with skrim
- **Section**: Expandable panels
- **URL**: components/panel/expandable-panel-skrim
- **Tags**: 
```tsx
import { VisaMediaFastForwardTiny, VisaMediaRewindTiny } from '@visa/nova-icons-react';
import {
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  PanelToggle,
  Typography,
  useFocusTrap,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';

export const ModalExpandablePanelWithSkrim = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <Utility vFlex>
      <UtilityFragment vMarginLeft="auto">
        <PanelToggle
          aria-expanded={false}
          aria-label="Open panel"
          buttonSize="large"
          iconButton
          iconTwoColor
          onClick={() => ref.current?.showModal()}
        >
          <VisaMediaRewindTiny rtl />
        </PanelToggle>
      </UtilityFragment>

      <UtilityFragment vMarginLeft="auto">
        <Panel
          expandable
          onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
          ref={ref}
          skrim
          style={{ height: 400 }}
          tag="dialog"
        >
          <PanelToggle
            aria-expanded="true"
            aria-label="Close panel"
            buttonSize="large"
            iconButton
            iconTwoColor
            onClick={() => ref.current?.close()}
          >
            <VisaMediaFastForwardTiny rtl />
          </PanelToggle>

          <PanelContent>
            <PanelHeader>
              <Typography tag="h2" variant="headline-3">
                Panel title
              </Typography>
            </PanelHeader>
            <PanelBody>
              <Typography tag="h3" variant="subtitle-2">
                Panel subtitle
              </Typography>
              <Typography>
                This is required text that can be used to describe the panel title and subtitle in more detail.
              </Typography>
            </PanelBody>
          </PanelContent>
        </Panel>
      </UtilityFragment>
    </Utility>
  );
};

```

### Tabbed modal expandable panel
- **Section**: Tabbed panels
- **URL**: components/panel/tabbed-expandable-panel
- **Tags**: 
```tsx
import { VisaMediaFastForwardTiny, VisaMediaRewindTiny } from '@visa/nova-icons-react';
import {
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  PanelToggle,
  Typography,
  useFocusTrap,
  Utility,
  PanelTabs,
  Button,
  UtilityFragment,
  Tab,
  Divider,
} from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'tabbed-expandable-panel-example';

const tabs = ['FAQ', 'Chat', 'Contact'];

export const TabbedModalExpandablePanel = () => {
  const { onKeyNavigation, ref } = useFocusTrap();
  const [selectedTabIndex, setSelectedTabIndex] = useState(0);

  return (
    <Utility vFlex>
      <UtilityFragment vMarginLeft="auto">
        <PanelToggle
          aria-expanded={false}
          aria-label="Open panel"
          buttonSize="large"
          iconButton
          iconTwoColor
          onClick={() => ref.current?.showModal()}
        >
          <VisaMediaRewindTiny rtl />
        </PanelToggle>
      </UtilityFragment>

      <UtilityFragment vMarginLeft="auto">
        <Panel
          expandable
          onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
          ref={ref}
          style={{ height: 400 }}
          tag="dialog"
        >
          <PanelToggle
            aria-expanded="true"
            aria-label="Close panel"
            buttonSize="large"
            iconButton
            iconTwoColor
            onClick={() => ref.current?.close()}
          >
            <VisaMediaFastForwardTiny rtl />
          </PanelToggle>

          <PanelContent>
            <PanelTabs orientation="horizontal" role="tablist">
              {tabs.map((tab, index) => (
                <Tab key={id + tab} role="none">
                  <Button
                    aria-label={tab}
                    aria-selected={index === selectedTabIndex}
                    buttonSize="large"
                    colorScheme="tertiary"
                    onClick={() => setSelectedTabIndex(index)}
                    role="tab"
                  >
                    {tab}
                  </Button>
                </Tab>
              ))}
            </PanelTabs>
            <Divider dividerType="decorative" />
            <PanelHeader>
              <Typography tag="h2" variant="headline-3">
                Panel title
              </Typography>
            </PanelHeader>
            <PanelBody>
              <Typography tag="h3" variant="subtitle-2">
                Panel subtitle
              </Typography>
              <Typography>
                This is required text that can be used to describe the panel title and subtitle in more detail.
              </Typography>
            </PanelBody>
          </PanelContent>
        </Panel>
      </UtilityFragment>
    </Utility>
  );
};

```

### Tabbed responsive expanded panel
- **Section**: Tabbed panels
- **URL**: components/panel/tabbed-expandable-responsive-panel
- **Tags**: 
```tsx
import { VisaMediaFastForwardTiny, VisaMediaRewindTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  PanelTabs,
  PanelToggle,
  Tab,
  Typography,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'tabbed-expandable-responsive-panel-example';

const tabs = ['FAQ', 'Chat', 'Contact'];

export const TabbedExpandableResponsivePanel = () => {
  const [open, setOpen] = useState(true);
  const [selectedTabIndex, setSelectedTabIndex] = useState(0);

  return (
    <Utility vFlex style={{ minBlockSize: 200 }}>
      <UtilityFragment vMarginLeft="auto">
        <PanelToggle
          aria-expanded={open}
          aria-label={open ? 'Close panel' : 'Open panel'}
          buttonSize="large"
          iconButton
          iconTwoColor
          onClick={() => setOpen(open ? false : true)}
        >
          {open ? <VisaMediaFastForwardTiny rtl /> : <VisaMediaRewindTiny rtl />}
        </PanelToggle>
      </UtilityFragment>

      {open && (
        <Panel expandable>
          <PanelContent>
            <PanelTabs orientation="horizontal" role="tablist">
              {tabs.map((tab, index) => (
                <Tab key={id + tab} role="none">
                  <Button
                    aria-label={tab}
                    aria-selected={index === selectedTabIndex}
                    buttonSize="large"
                    colorScheme="tertiary"
                    onClick={() => setSelectedTabIndex(index)}
                    role="tab"
                  >
                    {tab}
                  </Button>
                </Tab>
              ))}
            </PanelTabs>
            <Divider dividerType="decorative" />
            <PanelHeader>
              <Typography tag="h2" variant="headline-3">
                Panel title
              </Typography>
            </PanelHeader>
            <PanelBody>
              <Typography tag="h3" variant="subtitle-2">
                Panel subtitle
              </Typography>
              <Typography>
                This is required text that can be used to describe the panel title and subtitle in more detail.
              </Typography>
            </PanelBody>
          </PanelContent>
        </Panel>
      )}
    </Utility>
  );
};

```

## Property Sections
### Panel
- **Selector**: <Panel />
- **Description**: Collapsible or persistent containers used to present supplementary information.

### PanelBody
- **Selector**: <PanelBody />
- **Description**: Container for panel body elements.

### PanelContent
- **Selector**: <PanelContent />
- **Description**: Container for all panel content, included heading and body.

### PanelHeader
- **Selector**: <PanelHeader />
- **Description**: Container for panel heading.

### PanelToggle
- **Selector**: <PanelToggle />
- **Description**: Button used with a panel component to hide or show the panel.

### useFocusTrap
- **Selector**: None
- **Description**: This hook is used to trap focus inside a container.

## Properties
### expandable
- **Section**: Panel
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Expandable

### ref
- **Section**: Panel
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### responsive
- **Section**: Panel
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Responsive

### skrim
- **Section**: Panel
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Adds darker backdrop for modal panels

### tag
- **Section**: Panel
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: PanelBody
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: PanelBody
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: PanelContent
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### surfaceType
- **Section**: PanelContent
- **Type**: "alternate"
- **Default**: 
- **Required**: false
- **Description**: Type of Surface

### tag
- **Section**: PanelContent
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: PanelHeader
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: PanelHeader
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### alternate
- **Section**: PanelToggle
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: PanelToggle
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: PanelToggle
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: PanelToggle
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: PanelToggle
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: PanelToggle
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: PanelToggle
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: PanelToggle
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: PanelToggle
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: PanelToggle
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: PanelToggle
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag (not compatible with element property)

