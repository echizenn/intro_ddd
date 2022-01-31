"""
4.5.1節のコードの説明
"""

# リスト4.13
class PhysicalDistributionBase:
    """
    物流拠点エンティティ

    Attributes: 略
    """
    def ship(baggage: Baggage) -> Baggage:
        """
        出庫

        Args:
            baggage (Baggage): 出庫する荷物
        
        Returns:
            Baggage: 出庫する荷物

        Note:
            実装はしません
        """
        pass

    def receive(baggage: Baggage):
        """
        入庫

        Args:
            baggage (Baggage): 受け取る荷物
        
        Returns: None

        Note:
            実装はしません
        """
        pass