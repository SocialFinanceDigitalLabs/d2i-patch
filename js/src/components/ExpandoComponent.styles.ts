import styled from "@emotion/styled";
import { spacing } from "@sfdl/sf-mui-components";

export const Pre = styled.pre`
  white-space: normal;
  word-wrap: break-word;
`;

export const Aligner = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
`;

export const Justifier = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: start;
`;

export const SpaceBetween = styled.div`
  margin-right: ${spacing.m};
`;

export const PaddedBox = styled.div`
  margin: 0 ${spacing.s};
`;
